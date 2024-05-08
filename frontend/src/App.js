import React, { useState } from 'react';

const ImageUploader = () => {
    const [image, setImage] = useState(null);
    const [name, setName] = useState(null);

    const handleImageChange = (event) => {
        const file = event.target.files[0];
        setName(file.name)
        const reader = new FileReader();

        reader.onload = function(event) {
            const base64Image = event.target.result;
            setImage(base64Image);
        };

        reader.readAsDataURL(file);
        console.log()
    };

    const uploadImage = () => {
        // Prepare JSON object with image data
        const imageData = {image,name};
        // console.log(image)
        // console.log(image)

        // Send the JSON object to the backend
        fetch('https://image-to-url-link-testing.onrender.com//base64_to_url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                Accept:'application/json'
            },
            body: JSON.stringify(imageData)
        })
        .then((res) => res.json())
        .then(response => {
            // Handle response from server
            console.log(response);
        })
        .catch(error => {
            console.error('Error uploading image:', error);
        });
    };

    return (
        <div>
        <h2 className='text-red-500'>ok Tests</h2>
            <input type="file" onChange={handleImageChange} />
            <button onClick={uploadImage}>Upload Image</button>
        </div>
    );
};

export default ImageUploader;
