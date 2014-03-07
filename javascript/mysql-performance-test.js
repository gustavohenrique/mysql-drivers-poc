'use strict';

var mysql = require('mysql');

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'smartia'
});
 
connection.connect();

var sql = "SELECT cotacao.id FROM Pedido pedido FORCE INDEX (IDX_SMARTIA_BI) JOIN Cotacao cotacao ON cotacao.pedidoOrigem_id = pedido.id JOIN ResultadoCotacao resultado ON resultado.cotacao_id = cotacao.id WHERE NOT EXISTS (SELECT id FROM CotacaoAnalisada analisada WHERE analisada.id = cotacao.id) AND pedido.tipoCriador = 'INTERNET'";

connection.query(sql, function(err, rows, fields) {
    for (var i in rows) {
        console.log(rows[i].id);
    }
});

connection.end();
