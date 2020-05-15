from django.db import models
BIG_STRING = 60000

class Source(models.Model):
    title = models.CharField(max_length=BIG_STRING)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=BIG_STRING)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=BIG_STRING, unique=True)
    characters = models.ManyToManyField(Character)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class CharacterDescription(models.Model):
    body = models.CharField(max_length=BIG_STRING)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    class Meta:
        ordering = ['body']

    def __str__(self):
        return self.body

class Question(models.Model):
    body = models.CharField(max_length=BIG_STRING)
    order = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.body

class Answer(models.Model):
    body = models.CharField(max_length=BIG_STRING)
    characters = models.ManyToManyField(Character)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        ordering = ['body']

    def __str__(self):
        return self.body
