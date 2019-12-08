# -*- coding:utf8 -*-
import SocketServer
import os,random,signal
from string import hexdigits
from hashlib import md5
from secret import flag, m1, m4, password

class Task(SocketServer.BaseRequestHandler):
    def proof_of_work(self):
        random.seed(os.urandom(8))
        part_hash = "".join([random.choice(hexdigits) for _ in range(5)]).lower()
        salt = "".join([random.choice(hexdigits) for _ in range(4)]).lower()
        self.request.send("[*] Please find a string that md5(str + " + salt + ")[0:5] == %s\n" % (part_hash))
        self.request.send('[>] Give me xxxxx: ')
        string = self.request.recv(10)
        string = string.strip()
        if (md5(string + salt).hexdigest()[:5] != part_hash):
            self.request.send('[-] Wrong hash, exit...\n')
            return False
        return True

    def getM(self):
        return random.getrandbits(512)

    def level1(self):
        self.dosend('n = 8788243810113198481764566947869508914607026957466489668727548073613496825679400591687813426342686034806081353790472216192635172094987395128834590030497381\n')
        self.dosend('e1 = 2333\n')
        self.dosend('e2 = 23333\n')
        self.dosend('c1 = 4799918654649006116940502215835347906203162902787669199307383957409192303134738166614010930829808272183136103896570661157044610508330743272839870684458619\n')
        self.dosend('c2 = 3517433402358387844096791333634390193378704559086526036995918508702312833687284786927630246590107124972191795462221141049323183791880150003945625070468406\n')
        self.dosend('Please input your answer:\n')
        self.dosend('[>] ')
        ans1 = int(self.request.recv(1024).strip())
        if ans1 != m1:
            return False
        return True

    def level2(self):
        m2 = self.getM()
        n = 607900813663611067842837524661267364301550704378227659881901452531297221475040636195628925575855229656282223892087050493227081440280659712928800534490346879220642831988621810921598187433437378837837143501351423729677882983853496149047999678671286086457392694329911623356267250125698473655142476732580600637746199649870687527976434678329761718780196549933383562521810097843739766366411336632451675251205900001776144878467197785994504653053952116694201789023197153385339005092459140666207222691088762923508773221128431115940139639127361682894161575447178762249825640016917855258140241450958323555091405995851890923440318847524315885746456192524770784189513289482148237295117819525443770282328848309513469786825609469896483501821174911696076686122297451140515020902016476221555394631405807748304247062188071900702260272695809537710337210815836949969412320526240794719406618313088181764869343466599137077245401564928600711478908683466984267995973337332645121946601867073615045820510942656153543468965306446587268635504217564304202312293009330282199667043729023574994279506013458408920599612106410777171455809662951090003618715140536175558669535844334773825915679243838049185760728893699819949132064423885220963263250131219088767339535983
        e = 3
        c = hex(pow(m2,e,n))
        self.dosend('n = %s\n' % hex(n))
        self.dosend('e = 3\n')
        self.dosend('c = %s\n' % c)
        self.dosend('Please input your answer:\n')
        self.dosend('[>] ')
        ans2 = int(self.request.recv(1024).strip())
        if ans2 != m2:
            return False
        return True

    def level3(self):
        m3 = self.getM()
        n = 29705228213754565882993139471924572295182343211238615829181137202064051706595393267370754841943355967012677568512988647611509327120950259780728925515193851841761087515458718194800284149961389534872168019329253953209931011703282420411297656915759784139955772494392206450301449559319429509030460398915047980527018882610609013753981325385909414494476597636510759522537411097279302654844180412078439700626915272553559160209950455638217411089216829715434297244252794703847300018681207359956597466890846034383058641813812360626900475225731629387466381849160081144528650315470298268936500064362564132742099920530316819561869
        e = 65537
        c = hex(pow(m3,e,n))
        self.dosend('n = 0xeb4f8c45336c229371fd73a252b24dd3bf8b3cdc1bb1864f140fd63c88d47c44ba228bebe223fe53c7eaf88678b780821a6660b2726506216554990a5dda178ee04a47c7f1974fc8f8268d081bbb2be7e7353ccf36fecfce5f5f82722d064928f2d60844373c52b4d1db9dc41f7f16807c5b4356c4d2290811e25c51ef1227aa6e893d37dd8743e391fa638d77d0c55e4fb331576602128333d4be95f06523521e7511b39fc20111c88f2635b67e3531684d58ea6574179b5e63a862d073241f5ff91c97a45aa3d8e3287d8161a97728d2e19d72669f39f9e6ad10677bb563bdef30d0dcfa719c2f1836bd02b73d21dbecc11717b54c45d415d3f423ce6dfd8dL\n')
        self.dosend('e = 0x10001\n')
        self.dosend('p>>448 = 0xfb2151c701f7667b53822fe625b95edee00c3a947b234eca47903ef62fb128d813a9c1acb328f3f7181d24ce31814cd1a69ac4b61b269e2b0eb7fbaabe9633d33a36d0715b4cd386L\n')
        self.dosend('c = %s\n' % c)
        self.dosend('Please input your answer:\n')
        self.dosend('[>] ')
        ans3 = int(self.request.recv(1024).strip())
        if ans3 != m3:
            return False
        return True

    def level4(self):
        self.dosend('n1 = 0xb08bab371e516b9ac3a9c68bc2af143893aac7534ace6c172c6da6e8c7b8b0631819b2647b92d33c064bef0f6af50736a3897b7230771c315f4c4a7315c23691e5b859764f5968e9e623ac768d14bf4cdb9b56fb5b5d53236bf13a7b50bb247a9fe30e5d16c6c7ff34f875677a9438e2f1d0e4dee48c0141e697fef3881d91249ecf9c415d3846bbd8bf9ddec2229f7a13e3b0c085ec1073bc4b7d2654115967798244068e78bf2d150e702766ba7508d19346671a468943ca74509cb4fd7f8099b6a69f90f4ecf7326efc5584ebae592d3bc4ed54f5edd9c33f7a1880fa24f96a8317e52986fed69950f4243422e1ede448ba72894201ea47e23ec8157cf507L\n')
        self.dosend('n2 = 0xae8a5a3e9946f573c2b89167d2c4f7f630889c05a38b64f6f8ffe3e5230c946a065c19eab4f0b8caa75fdb3fdaa1e4f0e5f89baff4398c1a1fd32b292ac1c1d87a718c8ae3f58c2e6f97eb459dbaf1ffdc00d8b6e915c84c11dec00120308dc6e2b6778b953df6d9f454053c25db701987b89ece4de709a1b345a7528c4245ae3965b8ef29abcb278dc941fea5cbb369c74434c7b1e873ee2f6dc18bc5a69692358bf9443edb6b2eaeb674407ef763c62d57468e99408ef2fbb73699908e532de91689e07b77d12be0a425686b21aff40287749e391b4f46abecccba99d59d4ed861f57f1c520e888252be390245029808f07bfbd6e5200adff705b8255c93adL\n')
        self.dosend('e1 = 0x4628a2\n')
        self.dosend('e2 = 0x1436ea\n')
        self.dosend('c1 = 0x68efd78bd67438de2474bb1b9112e305266245359807dda408e9937bc97ee06d0098a8823cc49c562392361d15852f5dce226cc0651da86654228ed9c6a2cb4952b8b447f4deaff8b622030f41f3e506431362c7900c32f0e6e53b4eb43b6ab6358e1fdfd03bead43d61d35d292ef9f575dd7507ad24838ff27be4bf9f8221bf5eeccb460168c3f2d703edc8733a40d0d890cdb9584bb454886c74cdd69dee19855b80789ffe74088326f963e24c31c8e293f630cb6bac282ac49ad142c4d4fd90b272abe924ffa72c1b974cd90e0a41c80b40df6f492b63edb792cc48ff30e5aad7e5a1d8c021a1705c27692bf07f836530627f0a178b93b626ac6ebad06a71L\n')
        self.dosend('c2 = 0x3a9e0e7765e488f6f6651fa9758b99329beb2fb8117e990683e833a4c0a8203621fe69790ebcd4e99b7c7135753c6a6e785a206c6f668c541600f075a67d1df77c536e0659a6aee5291726da62b6b19d35bb3429eb5af41ee9b60c0f7ae28cb983428c7041fec0b5649dde69355c12795ed2a539458991164b35b37fa2495d8df80710cb75b64ae9ecfddf80fb188df864acac136c0cb9db0953e5328280ccbcd3dc8c32755045ffe0e59f38d3a5d2507d4123789681534d4a69020ad984839db68d437f0a5fc4542b5856e8845afa890e18217b34e4095511abe10787268aac55ceed1453fc5dc5c97593a4374b6603c439638c604c53282a6fb3f327a72518L\n')
        self.dosend('Please input your answer:\n')
        self.dosend('[>] ')
        ans4 = int(self.request.recv(1024).strip())
        if ans4 != m4:
            return False
        return True


    def level5(self):
        self.dosend('n = 19442176928007830098424428955804863422490104569894359496453939957229742423661160054241621640185600142526048820896573841917260538353760477502624635228772623542594808126714949387688256798485777301116254045665123490080599759063595943183174257000621175533455527351901382362223186460177724406923578989734811261651935021211994078268472388527276207734500306479937257181713076303044191424255541575089667633199235148135321345062563193566412742338012981130056909856454878804112411630977554868340858807585375893503827768149367059669895608437969230531174624250114738703422569825794356115744480899464005839030338854022395818875403\n')
        self.dosend('e = 5\n')
        self.dosend('c1 = 265062189690110258168937914660953141176262450217439754228412476921446090800865485245586374925301693092500339299234605734070010071396874397183777663814494638701287154485422437592402905249840040151974080315867776147021284075889623873125652375381248465118406871808612192648463354603146409805633298150440609502952012219466107223073722611710202703260376132210869385568895215174665401985520571514194067663539459950606936108462665901877112231914464806764529803480944795681849082656461363871269771058326378629532466874107079842249414630772189064960956110663544293311957887794906286805610383928125\n')
        self.dosend('c2 = 265062189690110258168937914660953141176262450217439754228412476921446090800865485245586374925301693092500339299234590972683684007932856122076633527469285284664876765956238156745882235870289890666905903061370680974052073327856401906558796495792640707398188184589372197560239909882241253361848467451770502253350255829962879608858461099793337589915413779774088831454734857389908802396033544417778902965804114905575051102617369791505746948583147955602054499061020529118234065874742791346925068898605296740979453445839143999750142181455751998618406840614227878335038410646539032726011271740251\n')
        self.dosend('Please input the password:\n')
        self.dosend('[>] ')
        ans5 = self.request.recv(1024).strip()
        if ans5 != password:
            return False
        return True

    def dosend(self, msg):
        try:
            self.request.sendall(msg)
        except:
            pass

    def handle(self):
        signal.alarm(500)
        if not self.proof_of_work():
            return
        signal.alarm(450)
        while True:
            self.dosend('Welcome to this easyCrypto System. If you pass all the tests, you will get the flag.\n')
            self.dosend('[*] Level 1\n')
            if not self.level1():
                self.dosend('[-] Something wrong\n')
                return False
            self.dosend('[*] Level 2\n')
            if not self.level2():
                self.dosend('[-] Something wrong\n')
                return False
            self.dosend('[*] Level 3\n')
            if not self.level3():
                self.dosend('[-] Something wrong\n')
                return False
            self.dosend('[*] Level 4\n')
            if not self.level4():
                self.dosend('[-] Something wrong\n')
                return False
            self.dosend('[*] Level 5\n')
            if not self.level5():
                self.dosend('[-] Something wrong\n')
                return False
            self.request.send("Congratulations！The flag is %s\n" % flag)
            self.request.close()

class ForkedServer(SocketServer.ForkingTCPServer, SocketServer.TCPServer):
    pass


if __name__ == '__main__':
    HOST, PORT = '0.0.0.0', 80
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()