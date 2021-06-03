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