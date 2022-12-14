from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name="사용자명")
    useremail = models.EmailField(max_length=128, verbose_name="사용자이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    class Meta:
        db_table = 't_user'

    def __str__(self):
        return self.username