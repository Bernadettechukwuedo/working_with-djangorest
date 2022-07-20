from rest_framework import generics
from .models import Text
from .serializers import TextCreateSerializer, TextSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class TextCreateAPIView(generics.CreateAPIView):
    queryset = Text.objects.all()
    model = Text
    serializer_class = TextSerializer

    def create(self, request, *args, **kwargs):
        print(self.request.user)
        serializer = TextCreateSerializer(data=request.data)
        user = self.request.user

        if serializer.is_valid():
            text = serializer.create(serializer.validated_data, user=user)
            read_serializer = self.get_serializer(text)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)


class TextUpdateAPIView(generics.UpdateAPIView):
    model = Text

    def get_queryset(self):
        user = self.request.user
        return Text.objects.filter(user=user)
    serializer_class = TextSerializer


class TextListAPIView(generics.ListAPIView):
    model = Text

    def get_queryset(self):
        user = self.request.user
        return Text.objects.filter(user=user)

    serializer_class = TextSerializer


class TextDetailAPIView(generics.RetrieveAPIView):
    model = Text

    def get_queryset(self):
        user = self.request.user
        return Text.objects.filter(user=user)
    serializer_class = TextSerializer


class TextDeleteAPIView(generics.DestroyAPIView):
    model = Text

    def get_queryset(self):
        user = self.request.user
        return Text.objects.filter(user=user)
    serializer_class = TextSerializer
