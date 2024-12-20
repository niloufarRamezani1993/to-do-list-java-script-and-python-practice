let getInput = document.querySelector("input")
let btnSave = document.querySelector("button")
let todolist = []


// get text from input
let txtInput = function () {
    return getInput.value.trim()
}
let getLiList = function (i) {
    let list = document.getElementById("List")
    let li = document.createElement("li")
    li.classList.add("w-full","flex", "items-center", "justify-between" ,"px-2", "py-2", "transition-colors", "text-white" , "bg-gray-600",  "bg-opacity-70"  ,"rounded-lg");
    
    
    // text container
    let textContainer = document.createElement("div")
    textContainer.textContent = i
    textContainer.classList.add("flex-grow")

    // buttons
    let btns = function(btn){
        btn.classList.add(  "rounded-md" ,"mx-0.5", "py-0.5" ,"px-1" , "text-gray-600" ,"bg-gradient-to-t" ,"from-amber-500" ,"to-amber-300" )
        return btn;
    }
    let tickBtn = document.createElement("button");
    tickBtn.textContent= "tick"
    tickBtn = btns(tickBtn)
    let deleteBtn =document.createElement("button");
    deleteBtn.textContent ="delete"
    deleteBtn = btns(deleteBtn)
    
    
    // جایگاه دکمه ها
    let btnsContainer = document.createElement("div")
    btnsContainer.appendChild(tickBtn)
    btnsContainer.appendChild(deleteBtn)
    btnsContainer.classList.add("flex","items-center", "justify-end", "space-x-2")
    
    li.appendChild(textContainer)
    li.appendChild(btnsContainer)
    
    list.appendChild(li)
   
    tickBtn.addEventListener("click" , ()=>{
        textContainer.classList.toggle("line-through")
        tickBtn.style.display = "none";
    })
    deleteBtn.addEventListener("click" , ()=>{
        list.removeChild(li);
    })
}




btnSave.addEventListener("click", () => {
    let txt = txtInput()
    if (txt == "") {
        alert("its Empty!")


    } else {
        todolist.push(txt)
        getLiList(txt)
        getInput.value = ""
    }

})
