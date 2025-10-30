package com.warehouse.dao;

import java.sql.*;
import java.util.*;
import com.warehouse.model.POJOs;
import com.warehouse.util.DB;

public class ProductDAO {

    public List<POJOs> getAllProducts() {
        List<POJOs> list = new ArrayList<>();
        String sql = "SELECT * FROM products";

        try (Connection conn = DB.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                POJOs product = new POJOs(
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getInt("quantity"),
                    rs.getInt("threshold")
                );
                list.add(product);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
        return list;
    }

    public void addProduct(POJOs p) {
        String sql = "INSERT INTO products(name, quantity, threshold) VALUES (?, ?, ?)";
        try (Connection conn = DB.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setString(1, p.getName());
            ps.setInt(2, p.getQuantity());
            ps.setInt(3, p.getThreshold());
            ps.executeUpdate();

            System.out.println("✅ Product added successfully!");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
