from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import GroceryItem
from .serializers import GroceryItemSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_grocery(request, pk):
    try:
        groceryItem = GroceryItem.objects.get(pk=pk)
    except GroceryItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a grocery item
    if request.method == 'GET':
        serializer = GroceryItemSerializer(groceryItem)
        return Response(serializer.data)
    # delete a grocery item
    elif request.method == 'DELETE':
        groceryItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a grocery item
    elif request.method == 'PUT':
        serializer = GroceryItemSerializer(groceryItem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_groceries(request):
    # get all groceries
    if request.method == 'GET':
        groceries = GroceryItem.objects.all()
        serializer = GroceryItemSerializer(groceries, many=True)
        return Response(serializer.data)

    # create new grocery item
    if request.method == 'POST':
        serializer = GroceryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
