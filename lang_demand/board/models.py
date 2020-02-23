from django.db import models


# Create your models here.
# 자유 게시판
class Board(models.Model):
    # 제목
    title = models.CharField(max_length=300)
    # 내용
    content = models.TextField()
    # 작성자
    writer = models.CharField(max_length=60)
    # 비밀번호
    pwd = models.CharField(max_length=300)
    # 작성일
    writeDate = models.DateField()
    # 조회수
    hit = models.IntegerField(default=0)

    def __str__(self):
        return self.title + "/" + self.writer

    class Meta:
        db_table = 'board'
