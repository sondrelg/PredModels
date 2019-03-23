from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
import time


class ViewRequest(APIView):
    """
    Used to display incoming request
    """

    def post(self, request: Request):
        for i in range(3):
            time.sleep(0.5)
            print(i+1)
        print(f'Request body: {request.body}')
        return Response({'received_data': request.data}, 200)

