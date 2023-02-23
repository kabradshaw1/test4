import React from "react";
import AllPosts, { getPosts } from "./index";
import { render } from '@testing-library/react'
import axios from "axios";

jest.mock('axios');
const mockedAxios = axios as jest.Mocked<typeof axios>

describe('API call test', () => {
  describe('when API call is successful', () => {
    test('Should do a get request for all posts', async () => {
      axios.get.mockResolvedValue()
      const post = await getPosts;
      expect(post).toEqual('First Post')
    })
  });

  describe('when API call fails', () => {
    test('should return return emply post list', () => {

    })
  })
})

test('Should render post component', () => {

});