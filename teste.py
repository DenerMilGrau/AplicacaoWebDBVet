cpf = '12345678901'

cpf_f = '{0}.{1}.{2}-{3}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
float(cpf_f)
