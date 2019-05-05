import Vue from 'vue'
import Vuex, { Commit } from 'vuex'

Vue.use(Vuex)

export interface State {
  isLocalOnly: boolean
  userName: string
  userId: string
}

const state: State = {
  isLocalOnly: true,
  userName: '',
  userId: '',
}

export const getters = {
  localOnly (state: State) {
    return state.isLocalOnly
  },
  userName (state: State) {
    return state.userName
  },
  userId (state: State) {
    return state.userId
  }
}

const mutations = {
  userName (state: State, payload: string) {
    state.userName = payload
  },
  userId (state: State, payload: string) {
    state.userId = payload
  }
}

export const actions = {
  setUserName ({ commit }: { commit: Commit }, payload: string) {
    commit('userName', payload)
  },
  setUserId ({ commit }: { commit: Commit }, payload: string) {
    commit('userId', payload)
  }
}

export default new Vuex.Store({
  state,
  mutations,
  getters,
  actions
})
