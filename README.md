The goal is to implement our own data onto our website. Right now we are running into an issue with feedstation, where
our own inventory is being over written by the inventory of our vendors. 

I have a plan to cut feedstation out of the loop and create our own data management application that can be manipulated 
in the browser with after logging in.

Issue Explanation:
    The main goal here is to have our own system that can manage our inventory on our website. We have a warehouse in 
    Sacramento that contains about 140 products. Our websites inventory management as of this second is all done on the 
    backend of our website. We can go into menus and manually adjust inventory, or export product information into CSV 
    format, make changes in excel and import the result. This was a great system to start, as I could narrow down only 
    the products in our inventory. In order to scale the business we decided test the waters with uploading inventory 
    from a vendors warehouse, XDP, they offer a data sheet XLS file that is updated daily, and can be modified in Excel 
    and imported to the website. Great. But now our inventory is harder to adjust with excel because it's showing two 
    warehouses inventory. This can be negated by filtering by brand, and that worked fine as XDP's data shee only 
    provides data for THEIR brand. Later we had the idea to add more warehouses, with the use of a company called 
    FeedStation we were able to integrate with Alliant Power, Turn14 and Premier Wholesale Distributors. This seemed 
    like a fantastic solution and worked well to start. Then we noticed an issue. FeedStation collects the data from the 
    vendors, and adds that total inventory data to that product on the back end, that in turn shows on the front end in 
    our inventory field, they then show that information, formatted by warehouse location in the availability field. For
    example, if a product has 15 items in Kentucky, 12 in Nevada, 3 in Texas, this will show on the website like so:

    Inventory: 30

    Availability: Kentucky: 15 Nevada: 12 Texas: 3

    This was efficient, and helped boost sales as now Customers had an idea on where the products are coming from.
    Now for the issue, If we have 10 of this item in our inventory in Sacramento, this information is ignored leading to 
    instances where, if there are 0 in our vendors warehouses, and 5 in mine, that item shows:

    Inventory: 0

    Availability: N/A

    The part is not available for purchase. This is also an issue if another vendor has the part readily available but 
    we are not integrated with their inventory.

What do I want the app to do (baby steps):
    
    View and edit my current inventory, and export(from the app)/import(to the site) the inventory levels, as it allows 
    for import schedules using CSV. THIS IS THE MAIN GOAL.
    
How do I want users to interact with the data:
    
    We will have a web interface, blocked by a secure login.
    Users with admin privileges will be able to edit inventory.
    Something to do with SQL, idk yet this is new to me.

Must have features:
    
    Alert me when inventory reaches a critically low level
    Find inventory by keyword or part number
    Scalability

Other integrations or automations:
    
    I think we will have to connect to an API offered by Shipstation so track inventory being removed from our system.
    When an order is placed it is automatically sent to shipstation. If an order is being dropshipped, we cancel the 
    order in Shipstation, and if an order is shipped from us, a tracking label is created. I think we can use this to 
    our advantage to track what is actually leaving from our location to keep stock accurate if there are other future 
    vendors with duplicate part numbers.

Suggested Immediate Action Plan
    
    Set up user authentication with roles (even if only two users for now).
    Build the inventory dashboard using your current JSON/CSV structure.
    Implement CSV import/export for easy data updates.
    Apply your brand’s color scheme to the app’s UI.
    Deploy a test version to a simple cloud platform when ready.