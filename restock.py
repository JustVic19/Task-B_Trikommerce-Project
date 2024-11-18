def restock_inventory(available_items, inventory_records, current_day):
    '''
    ***********COMPLETE THIS FUNCTION***********
    This function is responsible for updating the stock/restock for a given day.
    ---------------
    Function Input:
    ---------------
    available_items: (integer) Available Tshirts from the previous day.
    inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
    current_day: (integer) Day number which you want to add as the current day. 

    ----------------
    Function Output:
    ----------------
    available_items:(integer) This function returns this integer which updates the available items at the current day.

    The function will also update the inventory_records (For restocking) for a given current day. It will also return "available_items".
    '''

    # Example logic for sales and restocking
    sales_today = 10  # Example sales for the current day
    restocked_items_today = 20  # Example restocked items for the current day

    # Update available items
    available_items = available_items - sales_today + restocked_items_today

    # Append the new record to the inventory records
    inventory_records.append((current_day, sales_today, restocked_items_today, available_items))

    return available_items