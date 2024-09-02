# Abstração - é simples - abstrair o programa 
# Log 
# herança - é um 
class Log: #Super class
    def _log(self,msg): #assinatura do método 
        raise NotImplementedError('Implemente o método log')

    def log_error(self,msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self,msg):
        return self._log(f'Success: {msg}')

class LogFileMixin(Log): # sub class
    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log): # sub class
    def _log(self, msg):
        print(f'{msg}({self.__class__.__name__})')

if __name__ == '__main__':        
    l = LogFileMixin()
    l.log_error('Mensagem de Erro')
    l.log_success('Mensagem de Sucesso')