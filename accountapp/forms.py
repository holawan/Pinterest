from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm) :
    def __init__(self,*args,**kwargs) :
        super().__init__(*args, **kwargs) 
        # id를 변경 불가능하게 한다. 
        self.fields['username'].disabled = True 
    
