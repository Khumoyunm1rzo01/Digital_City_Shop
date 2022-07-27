from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import *
from .seralizer import *
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

@api_view(['POST'])
def User_Register(request):
    first_name = request.POST.get('first_name')
    username = request.POST.get('username') 
    last_name = request.POST.get('last_name')
    password = request.POST.get('password')
    email = request.POST.get('email')
    company_name = request.POST.get('company_name')
    card = request.POST.get('card')
    address = request.POST.get('address')
    contact_number = request.POST.get('contact_number')
    b = User.objects.create(first_name=first_name, last_name=last_name, password=password, email=email, company_name=company_name, card=card, contact_number=contact_number, address=address, username=username)
    ser = UserSerializer(b)
    return Response(ser.data)


@api_view(['GET'])
def Get_Slider(request):
    slider = Product.objects.filter(rating=5)
    ser = ProductSerializer(slider, many=True)
    return Response(ser.data)


@api_view(['GET'])
def On_Sale(request):
    a = Product.objects.filter(on_sale=True)
    ser = ProductSerializer(a, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Get_Product_Last(request):
    a = Product.objects.filter().order_by('-id')[:6]
    ser = ProductSerializer(a, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Product_price(request):
    start = request.GET['start']
    end = request.GET['end']
    a = Product.objects.filter(price__gte=start, price__lte=end)
    ser = ProductSerializer(a ,many=True)
    return Response(ser.data)


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@api_view(['GET'])
def Join_Newsletter(request):
    user = request.user
    if user.news == False:
        user.news = True
    return Response(status=status.HTTP_200_OK)





@api_view(['GET'])
def product_id(request,pk):
    a = Product.objects.get(id=pk)
    ser = ProductSerializer(a)
    return Response(ser.data)

@api_view(['GET'])
def Get_Similar(request, pk):
    product = Product.objects.get(id=pk)
    for i in product.category:
        category_id = []
        category_id.add(i)
        c = Category.objects.filter(id=category_id)
        similars = Product.objects.filter(category=c)
    ser = ProductSerializer(similars, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getproduct(request):
    q = Product.objects.filter().order_by('-id')[:6]
    ser = ProductSerializer(q, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getreview(request):
    a = Review.objects.all()
    ser = ReviewSerializer(a, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getcomment(request):
    a = Comment.objects.all()
    ser = CommentSerializer(a, many=True)
    return Response(ser.data)

class Info_View(ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

@api_view(['GET'])
def Getblog(request, pk):
    a = Blog.objects.get(id=pk)
    ser = BlogSerializer(a)
    return Response(ser.data)


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@api_view(['POST'])
def Postcontact(request):
    user = request.user
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    s = Subject.objects.get(id=subject)
    b = Contact.objects.create(user=user, subject=s, message=message)
    ser = ContactSerializer(b)
    return Response(ser.data)


@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@api_view(['POST'])
def Postcomment(request):
    user = request.user
    website = request.POST.get('website')
    comment = request.POST.get('comment')
    c = Comment.objects.create(user=user, website=website, comment=comment)
    ser = CommentSerializer(c)
    return Response(ser.data)

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@api_view(['POST'])
def Postreply(request):
    reply_to = request.POST.get('reply_to')
    reply = Comment.objects.get(id=reply_to)
    user = request.user
    website = request.POST.get('website')
    comment = request.POST.get('comment')
    email = request.POST.get('email')
    d = Reply.objects.create(reply_to=reply, user=user, website=website, comment=comment, email=email)
    ser = ReplySerializer(d)
    return Response(ser.data)

@api_view(['GET'])
def Getcookies(request):
    a = Cookies.objects.all()
    ser = CookiesSerializer(a, many=True)
    return Response(ser.data)


@api_view(['GET'])
def Getprivacy(request):
    a = Privacy_Policy.objects.all()
    ser = Privacy_Policy_Serializer(a, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getabout(request):
    a = About.objects.all()
    ser = AboutSerializer(a, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getrequirements(request):
    b = Requirements.objects.all()
    ser = RequirementsSerializer(b, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Gettoptrends(request):
    c = Top_Trends.objects.last()
    ser = Top_Trends_Serializer(c)
    return Response(ser.data)

@api_view(['GET'])
def Getdelivery(request):
    d = Delivery_Options.objects.all()
    ser = Delivery_Options_Serializer(d, many=True)
    return Response(ser.data)

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@api_view(['GET'])
def Getorder(request):
    user = request.user
    e = Order.objects.filter(user=user)
    ser = OrderSerializer(e, many=True)
    return Response(ser.data)

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@api_view(['GET'])
def Getorderitem(request):
    user = request.user
    f = OrderItem.objects.filter(user=user)
    ser = OrderItemSerializer(f, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getshippingsdetail(request):
    g = Shipping_Detail.objects.all()
    ser = Shipping_Detail_Serializer(g, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getcategory(request):
    g = Category.objects.all()
    ser = CategorySerializer(g, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getcolor(request):
    g = Color.objects.all()
    ser = ColorSerializer(g, many=True)
    return Response(ser.data)

class Cart_View(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
@api_view(['GET'])
def Getcartdetail(request):
    i = CartDetail.objects.all()
    ser = CartDetailSerializer(i, many=True)
    return Response(ser.data)


@api_view(['GET'])
def Getbillingdetails(request):
    j = BillingDetails.objects.all()
    ser = Billing_Detail_Serializer(j, many=True)
    return Response(ser.data)

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@api_view(['POST'])
def Postbillingdetails(request):
    user = request.user
    country = request.POST.get('country')
    postcode = request.POST.get('postcode')
    city = request.POST.get('city')
    billing = BillingDetails.objects.create(user=user, country=country, postcode=postcode, city=city)
    return Response({'status': "Muvaffaqiyatli yaratildi!"})

@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@api_view(['POST'])
def Edit_Rating(request, pk):
    product = Product.objects.get(id=pk)
    rating = request.POST.get('rating')
    product.rating = rating
    product.save()
    return Response({'status': "Muvaffaqiyatli o'zgartirildi!"})
    


@api_view(['GET'])
def Count_Rating(request, pk):
    product = Review.objects.filter(product__id=pk)
    soni = len(product)
    stars = []
    for i in product:
        stars.append(i.rating)
    norma = sum(stars)/soni
    return Response({"soni":soni,"norma":norma})
            
    
    



@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@api_view(['POST'])
def Add_Cart(request):
    product = request.POST.get('product')
    product = Product.objects.get(id=product)
    user = request.user
    total = request.POST.get('total')
    a = Cart.objects.create(user=user, total=total)
    a.product.add(product)
    ser = CartSerializer(a)
    return Response(ser.data)




@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@api_view(['POST'])
def Add_Wishlist(request):
    user = request.user
    ads = request.POST.get('id') 
    a = Product.objects.get(id=ads)
    username = request.POST.get('username') 
    user1 = User.objects.get(username=username)
    b = Wishlist.objects.create(user=user1, product=a)
    ser = WishlistSerializer(b)
    return Response (ser.data)


@api_view(['GET'])
def Search_Blog(request):
    q = request.GET['text']
    result = Blog.objects.filter(text__icontains=q)
    ser = BlogSerializer(result, many=True)
    return Response(ser.data)

#########################################################

def Index(request):
    context = {
        
    }
    return render(request, 'dashboard-02.html', context)


def Default(request):
    context = {
        
    }
    return render(request, 'index.html', context)

def General(request):
    context = {
        
    }
    return render(request, 'general-widget.html', context)

def Chart(request):
    context = {
        
    }
    return render(request, 'chart-widget.html', context)

def Boxed_Layout(request):
    context = {
        
    }
    return render(request, 'box-layout.html', context)

def Social_App(request):
    context = {
        
    }
    return render(request, 'social-app.html', context)

def Blogs_Get(request):
    blog = Blog.objects.all()
    context = {
        'blog':blog,
    }
    return render(request, 'bloglist.html', context)


def Avatars(request):
    context = {
        
    }
    return render(request, 'avatars.html', context)

def Mahsulot(request):
    context = {
        'product': Product.objects.all(),
    }
    return render(request, 'product.html', context)

def Product_Page(request):
    context = {
        
    }
    return render(request, 'product-page.html', context)

def Product_List(request):
    context = {
        
    }
    return render(request, 'list-products.html', context)

def Payment_Details(request):
    context = {
        
    }
    return render(request, 'payment-details.html', context)

def Order_History(request):
    context = {
        
    }
    return render(request, 'order-history.html', context)

def Cart_function(request):
    context = {
        
    }
    return render(request, 'cart.html', context)

def Wish_List(request):
    context = {
        
    }
    return render(request, 'list-wish.html', context)

def Checkout(request):
    context = {
        
    }
    return render(request, 'checkout.html', context)

def Pricing(request):
    context = {
        
    }
    return render(request, 'pricing.html', context)

def Chat(request):
    context = {
        
    }
    return render(request, 'chat.html', context)

def User_Profile(request):
    context = {
        
    }
    return render(request, 'user-profile.html', context)

def Edit_profile(request):
    context = {
        
    }
    return render(request, 'edit-profile.html', context)

def Users_Cards(request):
    context = {
        
    }
    return render(request, 'user-cards.html', context)

def Bookmark(request):
    context = {
        
    }
    return render(request, 'bookmark.html', context)

def Tasks(request):
    context = {
        
    }
    return render(request, 'task.html', context)

def To_Do(request):
    context = {
        
    }
    return render(request, 'to-do.html', context)

def Contact_02(request):
    context = {
        
    }
    return render(request, 'contacts.html', context)

def Blog_01(request):
    context = {
        
    }
    return render(request, 'blog.html', context)

def Blog_Single(request):
    context = {
        'blog': Blog.objects.all()
    }
    return render(request, 'blog-single.html', context)