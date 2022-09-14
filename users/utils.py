from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def _create_user(
        self,
        email,
        password,
        username,
        birthdate,
        first_name,
        last_name,
        is_staff,
        is_superuser,
        **extra_fields,
    ):

        if not email:
            raise ValueError("Users should have an email address")
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            username=username,
            birthdate=birthdate,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self,
        email,
        password,
        username,
        birthdate,
        first_name,
        last_name,
        is_staff,
        **extra_fields,
    ):

        return self._create_user(
            email,
            password,
            username,
            birthdate,
            first_name,
            last_name,
            is_staff,
            False,
            **extra_fields,
        )

    def create_superuser(
        self,
        email,
        password,
        username,
        birthdate,
        first_name,
        last_name,
        is_staff,
        **extra_fields,
    ):

        return self._create_user(
            email,
            password,
            username,
            birthdate,
            first_name,
            last_name,
            is_staff,
            True,
            **extra_fields,
        )
