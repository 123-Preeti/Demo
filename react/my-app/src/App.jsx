import { useState } from 'react'
import './App.css'
import message from './message'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Message/>
    </>
  )
}

export default App
