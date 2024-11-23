from rest_framework.serializers import ModelSerializer
from home.models import Topic, Comment, Reply_to_Comment

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        read_only_fields = ('id',)



class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', )


class ReplyToCommentSerializer(ModelSerializer):
    class Meta:
        model = Reply_to_Comment
        fields = '__all__'
        read_only_fields = ('id', )


