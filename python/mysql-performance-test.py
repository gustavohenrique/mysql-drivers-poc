# coding = utf-8
import umysql

class Bi(object):
    DB_HOST = 'bi.rds.smartia.aws'
    DB_PORT = 3306
    DB_USER = 'smartia_jdbc'
    DB_PASSWD = 'smlSCEMfv0ewPUOsoiZAB9CYq3vCU9'
    DB_NAME = 'smartia_prd'

class Local(object):
    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_USER = 'root'
    DB_PASSWD = 'root'
    DB_NAME = 'smartia'


def executa_query(sql):
    cnn = umysql.Connection()
    banco = Local()
    cnn.connect (banco.DB_HOST, banco.DB_PORT, banco.DB_USER, banco.DB_PASSWD, banco.DB_NAME)
    rs = cnn.query(sql)
    for row in rs.rows:
        print row[0]
    cnn.close()

sql = """
SELECT cotacao.id
FROM Pedido pedido
FORCE INDEX (IDX_SMARTIA_BI)
JOIN Cotacao cotacao ON cotacao.pedidoOrigem_id = pedido.id
JOIN ResultadoCotacao resultado ON resultado.cotacao_id = cotacao.id
WHERE
  NOT EXISTS (SELECT id FROM CotacaoAnalisada analisada WHERE analisada.id = cotacao.id)
  AND pedido.tipoCriador = 'INTERNET'
"""

#SELECT cotacao.id FROM Pedido pedido FORCE INDEX (IDX_SMARTIA_BI) JOIN Cotacao cotacao ON cotacao.pedidoOrigem_id = pedido.id JOIN ResultadoCotacao resultado ON resultado.cotacao_id = cotacao.id WHERE NOT EXISTS (SELECT id FROM CotacaoAnalisada analisada WHERE analisada.id = cotacao.id) AND pedido.tipoCriador = 'INTERNET'

if __name__ == "__main__":
    executa_query(sql)