import React from 'react';
import '../styles/Pastors.css';
import Pastor1 from "../Components/images/Pastor1.jpg";
import Pastor2 from "../Components/images/Pastor2.jpg";
import Pastor3 from "../Components/images/Pastor3.jpg";

const Pastors = () => {
  const pastors = [
    {
      id: 1,
      name: 'Pastor Ken',
      image: Pastor1, // Update with actual image paths
      role: 'Senior Pastor'
    },
    {
      id: 2,
      name: 'Pastor Lydia',
      image: Pastor2,
      role: 'Associate Pastor'
    },
    {
      id: 3,
      name: 'Pastor Joy',
      image: Pastor3,
      role: 'Youth Pastor'
    }
  ];

  return (
    <div className="pastors-container">
      <h1 className="pastors-title">Our Pastors</h1>
      
      <div className="pastors-grid">
        {pastors.map((pastor) => (
          <div key={pastor.id} className="pastor-card">
            <div className="pastor-image-container">
              <img 
                src={pastor.image} 
                alt={`${pastor.name}`} 
                className="pastor-image"
              />
            </div>
            <h3 className="pastor-name">{pastor.name}</h3>
            <p className="pastor-role">{pastor.role}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Pastors;