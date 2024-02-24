# my_auth.py
from django.contrib.auth import get_user_model
from .custom_auth import *  # custom Auth성공시 True 아니면 False
from django.contrib.auth.models import User

UserModel = get_user_model()

class MyBackend(object):
    def authenticate(self, request, username=None, password=None):
        if check_if_user(username, password): # OO커뮤니티 사이트 인증에 성공한 경우
            
            try :
                if not ((user_id == "22980" or user_id == "TEST") and user_pw == "admin") :
                    user_img = get_user_img(username)
            except :
                user_img = ""
            

            try: # 유저가 있는 경우
                # user = UserModel.objects.get(username=username)
                user = User.objects.get(username=username)
                user.email = user_img
                user.save()
                print(user.first_name)

            except UserModel.DoesNotExist: # 유저 정보가 없지만 인증 통과시 user 생성
                # user = UserModel(username=username)
                # user.is_staff = False
                # user.is_superuser = False                
                # user.save()
                # 여기서는 user.password를 저장하는 의미가 없음.(장고가 관리 못함)
                print("2")
                pass
            return user
        else: # OO 커뮤니티 사이트 인증에 실패한 경우, Django기본 User로 감안해 password검증
            # logging.info("살패2")
            print("3")
            return None
            # try:
            #     user = UserModel.objects.get(username=username)
            #     if user.check_password(password) and self.user_can_authenticate(user):
            #         return user
            # except:
            #     return None

    def user_can_authenticate(self, user):
        is_active = getattr(user, 'is_active', None) # 유저가 활성화 되었는지
        return is_active or is_active is None # 유저가 없는 경우 is_active는 None이므로 True

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id) # 유저를 pk로 가져온다
        except UserModel.DoesNotExist:
            return None