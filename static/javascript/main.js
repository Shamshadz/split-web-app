console.log("javascript is working");

function increment() {

    const div = document.createElement('div');
    div.className = 'container my-3';
    
    div.innerHTML = `<h5>payee</h5>
                        <table>
                            <tr>
                                <th>Name:</th>
                                <td><input type="text" name="name"></td>
                            </tr>
                            <tr>
                                <th>pay:</th>
                                <td><input type="number" name="pay"></td>
                            </tr>
                        </table>
                        <button type="button" class="btn btn-info" onclick="decrement(this)">-</button>`;

    document.getElementById("addpayees").appendChild(div);
      
};

function decrement(input){

    document.getElementById("addpayees").removeChild(input.parentNode);
    
};