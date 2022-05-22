const input = document.getElementById('input')
const list = document.getElementById('list')
const spiner = document.getElementById('spiner')
const results = document.getElementById('results')

document.addEventListener('submit', async (e) => {
  e.preventDefault()
  // remove list items
  while (list.firstChild) {
    list.removeChild(list.firstChild)
  }
  // show spiner
  spiner.removeAttribute('class')
  spiner.setAttribute('class', 'spiner_container')
  // Save input value
  const name = input.value
  // insert title
  const h2 = document.createElement('h2')
  h2.innerHTML = 'Resultados de la búsqueda'
  // create fragmen to insert elemnts
  const fragment = new DocumentFragment()
  // get items from api
  const response = await fetch(`http://localhost:3001/search/${name}`)
  const items = await response.json()
  if (items.length === 0) {
    const li = document.createElement('li')
    li.innerHTML = 'No se encontraron Pokemons con ese nombre.'
    list.appendChild(li)
  } else {
    items.forEach(element => {
      // create li
      const li = document.createElement('li')
      // create figure
      const figure = document.createElement('figure')
      figure.setAttribute('class', 'figure')
      // create img
      const img = document.createElement('img')
      img.setAttribute('src', element.img)
      img.setAttribute('alt', element.name)
      // create figcaption
      const figcaption = document.createElement('figcaption')
      figcaption.innerHTML = element.name
      // Set figure with childrens img and figcaption elements
      figure.appendChild(img)
      figure.appendChild(figcaption)
      li.appendChild(figure)
      fragment.appendChild(li)
    })
  }
  // remove spiner
  spiner.removeAttribute('class')
  spiner.setAttribute('class', 'spiner_container_hidden')
  // reset input 
  input.value = ''
  // inser list
  list.appendChild(fragment)
})