import Cookies from 'js-cookie'

export const getAccessToken = () => Cookies.get('access_token')
export const getRefreshToken = () => Cookies.get('refresh_token')
export const isAuthenticated = () => !!getAccessToken()

export const authenticate = async () => {
    if (getRefreshToken()) {
        try {


            Cookies.set('access_token', tokens.access_token, { expires: inOneHour })
            Cookies.set('refresh_token', tokens.refresh_token)

            return true
        } catch (error) {
            redirectToLogin()
            return false
        }
    }

    redirectToLogin()
    return false
}