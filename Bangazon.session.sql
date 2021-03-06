SELECT * FROM bangazonapi_recommendation

INSERT INTO bangazonapi_recommendation (customer_id, product_id, recommender_id)
VALUES (4, 1, 2)

INSERT INTO bangazonapi_recommendation (customer_id, product_id, recommender_id)
VALUES (2, 2, 4)

INSERT INTO bangazonapi_recommendation (customer_id, product_id, recommender_id)
VALUES (7, 2, 4)

INSERT INTO bangazonapi_recommendation (customer_id, product_id, recommender_id)
VALUES (4, 7, 6)

SELECT * FROM bangazonapi_favorite

INSERT INTO bangazonapi_favorite (customer_id, seller_id)
VALUES (5, 4)

SELECT
                    p.id,
                    p.name,
                    p.customer_id,
                    p.price,
                    p.description,
                    p.quantity,
                    p.created_date,
                    pc.name AS category_name,
                    p.location,
                    p.image_path,
                    u.first_name || ' ' || u.last_name AS full_name
                FROM
                    bangazonapi_product p
                JOIN
                    bangazonapi_customer c on p.customer_id = c.id
                JOIN
                    bangazonapi_productcategory pc on p.category_id = pc.id
                JOIN
                    auth_user u ON c.user_id = u.id
                WHERE p.price > 1000