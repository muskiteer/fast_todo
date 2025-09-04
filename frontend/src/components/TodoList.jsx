import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchTodos, addTodo } from '../store/todoSlice';
import TodoItem from './TodoItem';

export default function TodoList() {
  const [newTodo, setNewTodo] = useState('');
  const dispatch = useDispatch();
  const { items, loading, error } = useSelector((state) => state.todos);

  useEffect(() => {
    dispatch(fetchTodos());
  }, [dispatch]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (newTodo.trim()) {
      dispatch(addTodo(newTodo));
      setNewTodo('');
    }
  };

  if (loading) return <div>Loading todos...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div className="todo-list">
      <h2>Your Todos</h2>
      
      <form onSubmit={handleSubmit} className="add-todo-form">
        <input
          type="text"
          value={newTodo}
          onChange={(e) => setNewTodo(e.target.value)}
          placeholder="Add a new todo..."
        />
        <button type="submit">Add</button>
      </form>
      
      <div className="todos-container">
        {items.length === 0 ? (
          <p>No todos yet. Add one!</p>
        ) : (
          items.map((todo) => <TodoItem key={todo.id} todo={todo} />)
        )}
      </div>
    </div>
  );
}