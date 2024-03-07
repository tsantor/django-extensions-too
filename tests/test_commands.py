import pytest
from django.core.files.storage import default_storage
from django.core.management import call_command

from django_project.myapp.models import FakeModel


# from django_prod.models import YourModel  # replace with one of your actual models
@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.mark.django_db
def test_delete_unreferenced_files(capsys):
    # Setup: create a file that is not referenced by any model
    unreferenced_file_path = "unreferenced.txt"
    with default_storage.open(unreferenced_file_path, "w") as f:
        f.write("This file is not referenced by any model")

    # Setup: create a file that is referenced by a model
    referenced_file_path = "referenced.txt"
    with default_storage.open(referenced_file_path, "w") as f:
        f.write("This file is referenced by a model")
    obj = FakeModel(file=referenced_file_path)
    obj.save()

    # Call the command in dry-run mode and check that it identifies the unreferenced file
    call_command("delete_unreferenced_files", dry_run=True)
    assert unreferenced_file_path in capsys.readouterr().out

    # Call the command not in dry-run mode and check that it deletes the unreferenced file
    call_command("delete_unreferenced_files")
    assert not default_storage.exists(unreferenced_file_path)

    # Check that the referenced file was not deleted
    assert default_storage.exists(referenced_file_path)
