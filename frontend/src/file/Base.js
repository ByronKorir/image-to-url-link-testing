import React, { useState } from 'react';

const ImageUploader = () => {
    const [image, setImage] = useState(null);
    const [name, setName] = useState(null);
    const [url,setUrl] = useState(null);
    const [file,setFile] = useState(null);

    const handleImageChange = (event) => {
        const file = event.target.files[0];
        setName(file.name)
        const reader = new FileReader();

        reader.onload = function(event) {
            const base64Image = event.target.result;
            setImage(base64Image);
        };

        reader.readAsDataURL(file);
        setFile(file)
        console.log()
    };

    const uploadImage = () => {
        // Prepare JSON object with image data
        const imageData = {image,name,file};
        // console.log(image)
        // console.log(image)

        // https://image-to-url-link-testing.onrender.com
        // Send the JSON object to the backend
        fetch('http://127.0.0.1:5000/base64_to_url', {
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
            setUrl(response.url)
            console.log(response);
        })
        .catch(error => {
            console.error('Error uploading image:', error);
        });
    };
    console.log(url)

    return (
        <div>
        <h2 className='text-red-500'>ok Tests</h2>
            <input type="file" onChange={handleImageChange} />
            <button onClick={uploadImage}>Upload Image</button>
        
        {url && (<img src={url} alt={name} />)}
        </div>
    );
};

export default ImageUploader;
