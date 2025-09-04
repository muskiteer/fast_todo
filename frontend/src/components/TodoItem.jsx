import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { deleteTodo, updateTodo } from '../store/todoSlice';

export default function TodoItem({ todo }) {
  const [isEditing, setIsEditing] = useState(false);
  const [editText, setEditText] = useState(todo.todo);
  const dispatch = useDispatch();

  const handleDelete = () => {
    dispatch(deleteTodo(todo.id));
  };

  const handleToggleDone = () => {
    dispatch(updateTodo({ id: todo.id, todo: todo.todo, done: !todo.done }));
  };

  const handleEdit = () => {
    setIsEditing(true);
  };

  const handleSave = () => {
    dispatch(updateTodo({ id: todo.id, todo: editText, done: todo.done }));
    setIsEditing(false);
  };

  const handleCancel = () => {
    setEditText(todo.todo);
    setIsEditing(false);
  };

  return (
    <div className="todo-item">
      {isEditing ? (
        <div className="edit-mode">
          <input
            type="text"
            value={editText}
            onChange={(e) => setEditText(e.target.value)}
            className="edit-input"
          />
          <button onClick={handleSave} className="save-btn">Save</button>
          <button onClick={handleCancel} className="cancel-btn">Cancel</button>
        </div>
      ) : (
        <div className="view-mode">
          <div className="todo-content">
            <input
              type="checkbox"
              checked={todo.done}
              onChange={handleToggleDone}
            />
            <span className={todo.done ? 'completed' : ''}>{todo.todo}</span>
          </div>
          <div className="todo-actions">
            <button onClick={handleEdit} className="edit-btn">Edit</button>
            <button onClick={handleDelete} className="delete-btn">Delete</button>
          </div>
        </div>
      )}
    </div>
  );
}