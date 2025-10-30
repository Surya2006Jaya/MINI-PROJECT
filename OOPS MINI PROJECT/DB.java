package com.warehouse.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DB {
    public static Connection getConnection() {
        Connection conn = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/warehouse_db", "root", "Surya@2006");
            System.out.println("✅ Database connected!");
        } catch (ClassNotFoundException e) {
            System.out.println("❌ MySQL Driver not found!");
        } catch (SQLException e) {
            System.out.println("❌ Connection failed: " + e.getMessage());
        }
        return conn;
    }
}
