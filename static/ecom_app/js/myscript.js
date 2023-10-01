

// Jquery part
$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2] 

    console.log("pid = ", id)

    $.ajax({
        type:"GET",
        url:"/pluscart", 
        data:{
            uid:id
        },
        success:function(data){
            eml.innerText=data.no_of_items
            document.getElementById("amount").innerText=data.amount 
            document.getElementById("total_amount").innerText=data.total_amount
            console.log("data = " , data )
        }
    })
})



$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2] 


    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            uid:id,
        },
        success:function(data){
            eml.innerText=data.no_of_items
            document.getElementById("amount").innerText=data.amount 
            document.getElementById("total_amount").innerText=data.total_amount
        }
    })
})


$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this

    console.log("hello", id)
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            uid:id,
        },
        success:function(data){
            document.getElementById("amount").innerText=data.amount 
            document.getElementById("total_amount").innerText=data.total_amount
            eml.parentNode.parentNode.parentNode.parentNode.remove() 
        }
    })
})



$('.plus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/plus_wishlist",
        data:{
            prod_uid:id
        },
        success:function(data){
            // alert(data.message)
            console.log("plus")
            window.location.href = `http://127.0.0.1:8000/product/${id}`
        }
    })
})


$('.minus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    $.ajax({
        type:"GET",
        url:"/minus_wishlist",
        data:{
            prod_uid:id
        },
        success:function(data){
            console.log("minus")
            window.location.href = `http://127.0.0.1:8000/product/${id}`
        }
    })
})