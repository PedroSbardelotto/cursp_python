# Abstração - é simples - abstrair o programa 
# Log 
# herança - é um 
class Log:
    def log(self,msg): #assinatura do método 
        raise NotImplementedError('Implemente o método log')
        

class LogFileMixin(Log):
    def log(self, msg):
        print(msg) 


if __name__ == '__main__':        
    l = LogFileMixin()
    l.log('Qaulquer coisa')