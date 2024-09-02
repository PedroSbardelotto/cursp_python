# Abstração - é simples - abstrair o programa
# Log
# herança - é um

from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:  # Super class

    def _log(self, msg):  # assinatura do método
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):  # sub class
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:',msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):  # sub class
    def _log(self, msg):
        print(f'{msg}({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Mensagem de Erro')
    lp.log_success('Mensagem de Sucesso')
    lf = LogFileMixin()
    lf.log_error('Mensagem de Erro')
    lf.log_success('Mensagem de Sucesso')
    
