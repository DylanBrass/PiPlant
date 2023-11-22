// AuthContext.js
import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(() =>{return localStorage.getItem('isAuthenticated') === 'true' || false})

    useEffect(() => {
        localStorage.setItem('isAuthenticated', isAuthenticated.toString())
    }, [isAuthenticated])
    const login = () => {
        setIsAuthenticated(true)
        window.location.href = "/"
    };

    const logout = () => {
        setIsAuthenticated(false)
        window.location.href = "/login"

    };

    const authError = () => {
        setIsAuthenticated(false)
        window.location.href = "/login"
    }


    return (
        <AuthContext.Provider value={{ isAuthenticated, login, logout, authError }}>
            {children}
        </AuthContext.Provider>
    )
}

const useAuth = () => {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context
};

export { AuthProvider, useAuth };