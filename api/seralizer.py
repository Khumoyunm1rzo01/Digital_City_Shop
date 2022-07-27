from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        depth = 1

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        depth = 1



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"




class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        depth = 1



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1



    

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'



class CookiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookies
        fields = '__all__'
        depth = 1


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class Privacy_Policy_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Privacy_Policy
        fields = "__all__"

class AboutSerializer(serializers.ModelSerializer):
    class Meta: 
        model = About
        fields = "__all__"

class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = "__all__"

class Top_Trends_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Top_Trends
        fields = "__all__"
        depth = 1


class Delivery_Options_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery_Options
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        depth = 1

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = OrderItem
        fields = "__all__"
        depth = 1

class Shipping_Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping_Detail
        fields = "__all__"
        depth = 1

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
        depth = 1

class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = "__all__"

class Billing_Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = BillingDetails
        fields = "__all__"
        depth = 1


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__" 
        depth = 1