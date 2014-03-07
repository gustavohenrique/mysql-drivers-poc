package net.gustavohenrique;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Main {

    public static void main(String[] args) {
        String dbUrl = "jdbc:mysql://localhost/smartia";
        String dbClass = "com.mysql.jdbc.Driver";
        String query = "SELECT cotacao.id FROM Pedido pedido FORCE INDEX (IDX_SMARTIA_BI) JOIN Cotacao cotacao ON cotacao.pedidoOrigem_id = pedido.id JOIN ResultadoCotacao resultado ON resultado.cotacao_id = cotacao.id WHERE NOT EXISTS (SELECT id FROM CotacaoAnalisada analisada WHERE analisada.id = cotacao.id) AND pedido.tipoCriador = 'INTERNET'";
        String username = "root";
        String password = "root";

        try {
            Class.forName(dbClass);
            Connection connection = DriverManager.getConnection(dbUrl, username, password);
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(query);
            while (resultSet.next()) {
                String result = resultSet.getString(1);
                System.out.println(result);
            }
            connection.close();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}