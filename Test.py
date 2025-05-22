class Test:
    def Dis(s):
        print("Self method called");

    def __init__(self):
        print("Init method called");    


#Object creation
T = Test();

T.Dis();