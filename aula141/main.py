from log import LogPrintMixin, LogFileMixin
# Testando a execução no main
lp = LogPrintMixin()
lp.log_error('Mensagem de Erro')
lp.log_success('Mensagem de Sucesso')
lf = LogFileMixin()
lf.log_error('Mensagem de Erro')
lf.log_success('Mensagem de Sucesso')