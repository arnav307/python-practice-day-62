with open('text.txt','w') as file_manager:
    function=lambda x,y: x*y
    file_manager.write("The multiplication is "+ str(function(3,4)))
    print(file_manager)