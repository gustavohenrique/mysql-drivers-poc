#include <stdlib.h>
#include <stdio.h>
#include <mysql.h>

main() {
   MYSQL *conn;
   MYSQL_RES *res;
   MYSQL_ROW row;
   char *server = "localhost";
   char *user = "root";
   char *password = "root"; /* set me first */
   char *database = "smartia";

   conn = mysql_init(NULL);

   if (!mysql_real_connect(conn, server,
         user, password, database, 0, NULL, 0)) {
      fprintf(stderr, "%s\n", mysql_error(conn));
      exit(1);
   }
   
   if (mysql_query(conn, "SELECT cotacao.id FROM Pedido pedido FORCE INDEX (IDX_SMARTIA_BI) JOIN Cotacao cotacao ON cotacao.pedidoOrigem_id = pedido.id JOIN ResultadoCotacao resultado ON resultado.cotacao_id = cotacao.id WHERE NOT EXISTS (SELECT id FROM CotacaoAnalisada analisada WHERE analisada.id = cotacao.id) AND pedido.tipoCriador = 'INTERNET'")) {
      fprintf(stderr, "%s\n", mysql_error(conn));
      exit(1);
   }
   res = mysql_use_result(conn);

   printf("Resultado:\n");
   while ((row = mysql_fetch_row(res)) != NULL)
      printf("%s \n", row[0]);
   
   mysql_free_result(res);
   mysql_close(conn);
}