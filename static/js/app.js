
toastr.options = {
   "closeButton": false,
   "debug": false,
   "newestOnTop": true,
   "progressBar": false,
   "positionClass": "toast-top-center",
   "preventDuplicates": true,
   "showDuration": "300",
   "hideDuration": "1000",
   "timeOut": "5000",
   "extendedTimeOut": "1000",
   "showEasing": "swing",
   "hideEasing": "linear",
   "showMethod": "fadeIn",
   "hideMethod": "fadeOut"
 }



 function getFullDateTime(){
     
   var today = new Date();
   var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
   var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
   return date+' '+time;
}
const hostname = window.location.origin + window.location.pathname


var c = new Vue({
    delimiters: ['{!','!}'],
    el: '#app',
    data: { 
        

      directory: 'Dashboard',
      //  products
        products: [],
        categories:[],
        order:{
            dir:1,
            column:'name'
        },

        filter:{
           name:''
        },

        product:{
           id:0,
           name:'',
           category:0,
           price:0,
           stock:0,
        },

        csrf_token:$('input[name="csrfmiddlewaretoken"]').val(),
        currentPage:1,
        perPage:5,
        errors: {},
        isEdit:false,

      //  logs here
      trans:[],

      
      

   },
   mounted(){
        
        this.fetchProducts(); 
        this.fetchCategories();
        this.fetchLogs();
   },
   computed:{
   

      pages(){
         return Math.ceil(this.products.length/this.perPage)
      },
      isFirstPage(){
         return this.currentPage === 1;
      },
      isLastPage(){
         return this.currentPage === this.pages;
      },
      paginateProducts(){
        let start = (this.currentPage - 1) * this.perPage
        ,end = this.currentPage * this.perPage

        return this.sortProducts.slice(start, end)
      },

      filteredProducts(){
         let products = this.products
         if(this.filter.name.length>0){
            let regxp = new RegExp(this.filter.name,'i')
            products =  products.filter(e =>
                e.name.match(regxp))
   
         }
         return products
      },

      sortProducts(){
         return this.filteredProducts.sort((a,b) => 
            {
               let left =  a[this.order.column],
                   right = b[this.order.column]

               if(isNaN(left) && isNaN(right)){
                  if(left>right)
                     return 1 * this.order.dir;
                  else if(left<right)
                     return -1 * this.order.dir;
                  else
                     return 0;
               }
               else
                  return (left-right) * this.order.dir;
            }
            
         ); 
           
      },
     
      sortType(){
         return this.order.dir === 1 ?'ascending':'descending'
      },
      


     

      isEmptyObject(){
         for(var key in this.errors){
            if(this.errors.hasOwnProperty(key)){
               return false;
            }
         }
         return true;
      },

      

   },

   methods:{ 
      prev(){
         if(!this.isFirstPage){
            this.currentPage--;
         }
      },
      next(){
         if(!this.isLastPage){
            this.currentPage++;
         }
      },

      classes(col){
         //return ['sort-control','ascending'];
         return ['sort-control',
            this.order.column === col ?this.sortType:''
         ]
      },
      sort(col){
         this.order.column = col
         this.order.dir *=-1
      },
      clearText(){
         this.filter.name = ''
      },

      saveProduct(){
            let target = hostname + (this.product.id?'product/'+this.product.id+'/update':'products/create')
            let data =  new FormData();
            data.append("name", this.product.name)
            data.append("price", this.product.price)
            data.append("category", this.product.category)
            data.append("stock", this.product.stock)
            data.append("csrfmiddlewaretoken",this.csrf_token)
            axios.post(target,data).
                     then((res) => {
                        $('#product_form').modal('hide');
                        toastr["success"](res.data.message)
                        this.fetchProducts()
                     }).catch(({response}) => {
                        // this.errors = response.data.errors
                     })
            this.clearProductModel()
      },

      

      fetchProducts(){
        
         axios.get(hostname+'products').
         then((response) => {
            this.products=response.data.products
         })
      },

      

      currentData(product){
         this.product.name= product.name
         this.product.category=product.category_id
         this.product.price = product.price
         this.product.id = product.id
         this.product.stock=product.stock
      },

      fetchCategories(){
         
         axios.get(hostname+'categories').
         then((response) => {
               this.categories = response.data.categories
            })
      },

      clearProductModel(){
         this.product.name= ''
         this.product.category=0
         this.product.price = 0
         this.product.id = 0
         this.product.stock = 0
      },

      deleteProduct(product){
         data = new FormData()
         data.append("csrfmiddlewaretoken",this.csrf_token)
         axios.post(hostname+'product/'+product.id+'/delete', data)
         .then(res => {
            toastr["warning"](res.data.message)
                  this.fetchProducts() 
               })
      },

      selectDirectory(dir){
         this.directory = dir
         this.active=1
       },

       fetchLogs(){
         axios.get(hostname+'logs').
         then((response) => {
               this.trans = response.data.logs
         })
       }
       ,

       isEmpty(obj){
         for(var key in obj){
            if(obj.hasOwnProperty(key)){
               return false;
            }
         }
         return true;
       }

   }
})


var ctx = document.getElementById("myChart");
      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
          datasets: [{
            data: [15339, 21345, 18483, 24003, 23489, 24092, 12034],
            lineTension: 0,
            backgroundColor: 'transparent',
            borderColor: '#007bff',
            borderWidth: 4,
            pointBackgroundColor: '#007bff'
          }]
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: false
              }
            }]
          },
          legend: {
            display: false,
          }
        }
      });