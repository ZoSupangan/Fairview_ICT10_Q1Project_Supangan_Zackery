import random
from pyscript import document, when


@when("click", "#btn-sku")
def generate_sku(event):
    name_input = document.querySelector('#sku-name').value.strip()
    category = document.querySelector('#sku-category').value
    size = document.querySelector('#sku-size').value
    output_div = document.querySelector('#sku-output')

    if not name_input:
        output_div.innerHTML = '<p class="placeholder-text" style="color: #c084fc;">Please enter a product name first.</p>'
        return

  
    clean_name = "".join(char for char in name_input if char.isalpha()).upper()
    name_code = clean_name[:3] if len(clean_name) >= 3 else clean_name.ljust(3, "X")
    
   
    batch_num = random.randint(100, 999)

    final_sku = f"SKW-{category}-{name_code}-{size}-{batch_num}"

    output_div.innerHTML = f'''
        <div class="sku-box">
            <div>Generated Item SKU</div>
            <div class="sku-code">{final_sku}</div>
        </div>
    '''


@when("click", "#btn-order")
def create_order(event):
    
    checkboxes = document.querySelectorAll('.menu-list input[type="checkbox"]:checked')
    output_div = document.querySelector('#receipt-output')
    
    if len(checkboxes) == 0:
        output_div.innerHTML = '<p class="placeholder-text" style="color: #c084fc;">Please select at least one item from the menu.</p>'
        return
    
    total = 0.0
    items_html = ""
    
    
    for item in checkboxes:
        name = item.getAttribute('data-name')
        price = float(item.value)
        total += price
        
        items_html += f'''
            <div class="receipt-row">
                <span>{name}</span>
                <span>₱{price:.2f}</span>
            </div>
        '''
        
    receipt_template = f'''
        <div class="receipt-title">Skewer Order Receipt</div>
        {items_html}
        <div class="receipt-total">
            <span>TOTAL</span>
            <span class="total-amount">₱{total:.2f}</span>
        </div>
    '''
    
    output_div.innerHTML = receipt_template