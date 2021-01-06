console.log('Hello')

const carsDataBox = document.getElementById('cars-data-box')
const carsModelBox = document.getElementById('models-data-box')

const carInput = document.getElementById('car-input')
const modelInput = document.getElementById('model-input')

const modelText = document.getElementById('model-text')


$.ajax({
    type: 'GET',
    url: '/cars-json/',
    success: function(response){
        console.log(response)
        const carsData = response.data

        carsData.map(item=>{
            const option = document.createElement('option')
            option.textContent = item.car_title
            option.setAttribute('value', item.car_title)
            carsDataBox.appendChild(option)
        })
    },
    error: function(error){
        console.log(error)
    }
})

carInput.addEventListener('change', e=>{
    console.log(e.target.value)
    const selectedCar = e.target.value

    carsModelBox.innerHTML=""
    modelText.textContent = "Model"

    $.ajax({
        type: 'GET',
        url: `models-json/${selectedCar}/`,
        success: function(response){
            console.log(response)
            const modelsData = response.data
            modelsData.map(item=>{
                const option = document.createElement('option')
                option.textContent = item.car_model
                option.setAttribute('value', item.car_model)
                carsModelBox.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})