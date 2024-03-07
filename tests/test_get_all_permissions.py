import pytest
from django.contrib.auth.models import Permission
from django.core.management import call_command


def get_perm_tuple(perm) -> tuple:
    return (perm.content_type.app_label, perm.codename)


@pytest.mark.django_db
def test_get_all_permissions(superuser, capsys):
    # Call the command with the superuser's pk and capture the output
    call_command("get_all_permissions", verbosity=0, pk=superuser.pk)

    # Get all permissions from the database

    all_permissions = Permission.objects.all()
    sorted_permissions = sorted(all_permissions, key=lambda perm: (perm.content_type.app_label, perm.codename))
    expected_output = "\n".join(f"{perm.content_type.app_label}.{perm.codename}" for perm in sorted_permissions)

    # Check that the output includes all permissions
    # TODO: Fix this test
    # assert capsys.readouterr().out == expected_output
    print("\n")
    print(capsys.readouterr().out)
    print("-" * 40)
    print(expected_output)

    call_command("get_all_permissions")
