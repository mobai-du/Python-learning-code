def send_alert(msg,*args):
    for users in args:
        print('报警发送给',users)

send_alert('别tm浪了',"alex","shanshan")

send_alert("别tm浪了",*['alex','shanshan','xxx'])


def func(name,*args,**kwargs):
    print(name,args,kwargs)

func('alex',22,'telsa','500w',add='山东',num=123123)

d = {'degree':"primary shcool"}
func('peiqi',**d)