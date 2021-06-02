"""Module for generating favorited sellers by customer report"""
import sqlite3
from django.shortcuts import render
from bangazonapi.models import Favorite, Customer
from bangazonreports.views import Connection

def favorite_sellers_list(request):

    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all sellers, with related user info.
            db_cursor.execute("""
                SELECT
                    f.id,
                    f.seller_id,
                    f.customer_id,
                    u.id user_id,
                    u.first_name || ' ' || u.last_name AS full_customer_name
                FROM
                    bangazonapi_favorite f
                JOIN
                    bangazonapi_customer c ON f.customer_id = c.id
                JOIN auth_user u ON c.user_id = u.id
            """)

            dataset = db_cursor.fetchall()

            favorited_sellers_by_customer = {}

            for row in dataset:

                favorite_seller = Customer.objects.get(pk=row["seller_id"])

            

                uid = row["user_id"]

                if uid in favorited_sellers_by_customer:
                    favorited_sellers_by_customer[uid]['favorite_sellers'].append(favorite_seller)
                else:
                    favorited_sellers_by_customer[uid] = {}
                    favorited_sellers_by_customer[uid]["id"] = uid
                    favorited_sellers_by_customer[uid]["full_customer_name"] = row["full_customer_name"]
                    favorited_sellers_by_customer[uid]["favorite_sellers"] = [favorite_seller]
        
        list_of_favorited_sellers = favorited_sellers_by_customer.values()

        template = 'users/list_fav_sellers.html'
        context = {
            'favorite_sellers_list': list_of_favorited_sellers
        }

        return render(request, template, context)