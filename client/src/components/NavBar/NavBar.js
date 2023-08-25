import { Stack, Box, Typography } from '@mui/material'
import { Link } from 'react-router-dom'

import { logo } from '../../utils/constants'
import SearchBar from '../SearchBar/SearchBar'

// replace Logo with FlatIron logo??
const NavBar = () => (
  <Stack
    direction="row"
    alignItems="center"
    p={2}
    sx={{ position: 'sticky', background: '#181818', top: 0, justifyContent: 'space-between' }}
  >
    <Link to="/" style={{ display: 'flex', alignItems: 'center' }}>
      <img src={logo} alt="logo" height={45} />
      <Box color="white" sx={{ flex: 2 }} >
        <Typography variant='h4' fontWeight="bold">
          FlatIron Tube
        </Typography>
      </Box>
    </Link>
    <SearchBar />
  </Stack>
)

export default NavBar