"""В этом модуле собраны основные модели, используемые в проекте."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель групп, используемых для объединения постов схожей тематики."""

    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель поста пользователей."""

    text = models.TextField()
    pub_date = models.DateTimeField(
        "Дата публикации", auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name="posts", blank=True, null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель для комментариев к постам пользователей."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    """Модель для реализации механизма подписи пользователей друг на друга."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Подписывающийся пользователь",
        related_name="follower",
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Подписываемся на пользователя",
        related_name="following",
    )

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "following"],
                       name="unique_subscribing",)
                       ]
