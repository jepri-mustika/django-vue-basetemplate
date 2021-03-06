from rest_framework import generics
from .serializers import QuestionSerializer

from .models import Question

class ListQuestionsView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
